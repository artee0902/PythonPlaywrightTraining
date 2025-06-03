from playwright.sync_api import Playwright

ordersPayload={{"productName":"","minPrice":null,"maxPrice":null,"productCategory":[],"productSubCategory":[],"productFor":[]}}


class APIUtils:

    def createOrder(self,playwright:Playwright):

        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        api_request_context.post("/api/ecom/product/get-all-products",data=ordersPayload,
                                                            headers={"authorization":token})



