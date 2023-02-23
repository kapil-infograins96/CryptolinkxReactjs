from rest_framework.views import APIView
import pandas as pd
from requests import Request, Session
import json
from rest_framework import status
from rest_framework.response import Response
from core.models import Wallet, Order, Crypto_wallet
from core.core_api.serializers import WalletSerializer, BuySerializer
from account.models import Custom_User
from rest_framework_simplejwt.backends import TokenBackend



class ExchangeViewAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:    
            symbol_list = None

            

            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': '49ac0cae-a97f-4a9e-a5f6-5e8a64fe39eb'
                
                

                
            }
            parameters = {}
            session = Session()
            session.headers.update(headers)
            response = session.get(url, params=parameters)
            info = json.loads(response.text)
            df = pd.DataFrame(info['data'])
            df['price'] = df['quote'].apply(lambda x : x['USD']['price'])
            df['percent_change_24h']=df['quote'].apply(lambda x:x['USD']['percent_change_24h'])       
            df['price'] = df['price'].apply(lambda x : "{:.6f}".format(x))
            df['percent_change_24h'] = df['percent_change_24h'].apply(lambda x : "{:.2f}".format(x))
            df = df[['symbol','price','name','percent_change_24h']]
            symbol_list = list(df.to_dict('index').values())

            context = {
                    "status":status.HTTP_200_OK,
                    "success": True,
                    "response":symbol_list
                    }

            return Response(context)

        
        except Exception as Exception:
            context = {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "success": False,
                    "response":str(Exception)
                    }

            return Response(context)


class WalletAPi(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            get_logged_in_user = valid_data['user_id']
            print(get_logged_in_user)
            get_user = Custom_User.objects.get(id=get_logged_in_user)

            get_wallet_details = Wallet.objects.get(user_id = get_user.id)
            print(get_wallet_details)
            print(get_wallet_details.user)
            print(get_wallet_details.Currency_type)
            print(get_wallet_details.money)


            serializer = WalletSerializer(get_wallet_details)

            content = {
           
            "status":status.HTTP_200_OK,
            "success":True,
            "response":serializer.data,
            }
            return Response(content,status=status.HTTP_200_OK)

        except Exception as e:
            context = {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "success": False,
                    "response":str(e)
                    }
            return Response(context)


class Buy_CryptoAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            get_logged_in_user = valid_data['user_id']
            
            get_user = Custom_User.objects.get(id=get_logged_in_user)

            if get_user:
           
                serializer = BuySerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    get_order_id = Order.objects.filter(user = get_user, type = "Buy" , status = "Completed") 
                    

                    
                    if get_order_id:
                        print("buy wala")
                        get_latest_order = Order.objects.filter(user = get_user).last()
                        
                        quantity = get_latest_order.quantity
                        invested = get_latest_order.invested_rs
                        crypto_name = get_latest_order.crypto_name
                        

                        
                        
                        for i in get_order_id:
                            get_wallet = Crypto_wallet.objects.filter(crypto_name = i.crypto_name).exists()
                            get_wallet_attr = Crypto_wallet.objects.filter(crypto_name = i.crypto_name).first()
                            

                        
                        if get_wallet :
                            pre_quantity = get_wallet_attr.quantity
                            pre_invested = get_wallet_attr.invested
                            print("phle wali values")
                            print(pre_quantity)
                            print(pre_invested)
                            


                            total_quantity  = pre_quantity + quantity
                            total_invested = pre_invested + invested
                            

                            get_wallet_attr.quantity = total_quantity
                            get_wallet_attr.invested = total_invested
                            get_wallet_attr.save()
                            
                        else:
                            wallet_create = Crypto_wallet(user_id = get_user.id, quantity = quantity, invested = invested, crypto_name = crypto_name)
                            wallet_create.save()

                            
                    
                   


                    else:

                        context = {
                                "status":status.HTTP_400_BAD_REQUEST,
                                "success": False,
                                "response":"sell or without oompleted order"
                                }
                        return Response(context)


                    content = {
                
                    "status":status.HTTP_201_CREATED,
                    "success":True,
                    "response":"sucess",
                    }
                    return Response(content,status=status.HTTP_201_CREATED)
        
        
        except Exception as e:
            context = {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "success": False,
                    "response":str(e)
                    }
            return Response(context)


class Sell_CryptoAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            get_logged_in_user = valid_data['user_id']
            
            get_user = Custom_User.objects.get(id=get_logged_in_user)

            if get_user:
           
                serializer = BuySerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    get_order_id = Order.objects.filter(user = get_user, type = "Sell" , status = "Completed") 

                    if get_order_id:
                        get_latest_order = Order.objects.filter(user = get_user).last()
                        quantity = get_latest_order.quantity
                        invested = get_latest_order.invested_rs
                        crypto_name = get_latest_order.crypto_name
                        print("=============post quantity============")
                        print(quantity)
                        print(type(quantity))
                        for i in get_order_id:
                            get_wallet = Crypto_wallet.objects.filter(crypto_name = i.crypto_name).exists()
                            get_wallet_attr = Crypto_wallet.objects.filter(crypto_name = i.crypto_name).first()

                        if get_wallet :
                            pre_quantity = get_wallet_attr.quantity
                            pre_invested = get_wallet_attr.invested
                            print("=============pre wallet quantity============")
                            print(pre_quantity)
                            print(type(pre_quantity))


                            if pre_quantity <= quantity:
                                print("ho gya")










        except Exception as e:
            context = {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "success": False,
                    "response":str(e)
                    }
            return Response(context)
                            








                

                   
                       


        
                    
                        

                       
                        


                
                
                    
                        

                       
                        


