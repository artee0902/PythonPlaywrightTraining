from playwright.sync_api import Playwright

ordersPayload={"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}


class APIUtils:



    def get_token(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post("/api/ecom/auth/login",
                                          data={"userEmail":"aartigorde999@gmail.com","userPassword":"Aarti@9420"})

        assert response.ok
        print(response.json())
        responseBody=response.json()

        return responseBody["token"]



    def createOrder(self,playwright:Playwright):

        token=self.get_token(playwright)
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post("/api/ecom/order/create-order",data=ordersPayload,
                                                            headers={"authorization":token,
                                                                     "content-type":"application/json"})

        print(response.json())
        response_body=response.json()
        orderID =  response_body["orders"][0]
        return orderID




