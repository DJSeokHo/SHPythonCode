from framewrok.module.http.http_wrapper import HTTPWrapper
from framewrok.utility.log_utility import ILog


if __name__ == '__main__':

    # 生成产品说明
    response = HTTPWrapper() \
        .url("https://api.openai.com/v1/chat/completions") \
        .header({
            "Content-Type": "application/json",
            "Authorization": "Bearer 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"
        }) \
        .body({
            "model": "gpt-3.5-turbo-1106",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a good product salesperson."
                },
                {
                    "role": "user",
                    "content": """
                    Consideration product : 工厂现货PVC充气青蛙夜市地摊热卖充气玩具发光蛙儿童水上玩具
                    1. Compose human readable product title used on Amazon in english within 20 words.
                    2. Write 5 selling points for the products in Amazon.
                    3. Evaluate a price range for this product in U.S.Output the result in json 
                    format with three properties called title, selling_points and price_range
                    """
                }
            ]
        }) \
        .post()

    ILog.debug(__file__, response)
