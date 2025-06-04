from playwright.sync_api import Playwright

payload={"productName":"","minPrice":"null","maxPrice":"null","productCategory":[],"productSubCategory":[],"productFor":[]}


class APIUtils:


    def get_token(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post("/api/ecom/auth/login",
                                          data={"userEmail":"aartigorde999@gmail.com","userPassword":"Aarti@9420"})

        assert response.ok
        print(response.json())
        responseBody=response.json()


        return responseBody["token"]

    def get_all_prducts(self,playwright:Playwright):
        token = self.get_token(playwright)

        api_requests=playwright.request.new_context(base_url="https://rahulshettyacademy.com")

        response=api_requests.post(url="api/ecom/product/get-all-products",
                                   data=payload,
                                   headers={"authorization":token,
                                              "content-type":"application/json"})









