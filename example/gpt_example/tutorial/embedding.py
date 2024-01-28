import json

from example.gpt_example.tutorial.gpt_constants import API_KET
from framewrok.module.http.http_wrapper import HTTPWrapper
from framewrok.utility.log_utility import ILog
import numpy


def get_embedding(content: str) -> list:
    text = content.replace("\n", " ")

    response = HTTPWrapper() \
        .url("https://api.openai.com/v1/embeddings") \
        .header({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KET}"
        }) \
        .body({
            "model": "text-embedding-3-small",
            "input": text
        }) \
        .post()

    response_dict: dict = json.loads(response)
    datas: list = response_dict["data"]
    data: dict = datas[0]
    embedding: list = data["embedding"]
    return embedding


def get_score(sample_embedding):
    return cosine_similarity(sample_embedding, positive_review) - cosine_similarity(sample_embedding, negative_review)


def cosine_similarity(vector_a, vector_b):
    dot_product = numpy.dot(vector_a, vector_b)
    norm_a = numpy.linalg.norm(vector_a)
    norm_b = numpy.linalg.norm(vector_b)
    epsilon = 1e-10
    return dot_product / (norm_a * norm_b + epsilon)


if __name__ == '__main__':
    """
    embedding: 这个 API 可以把任何你指定的一段文本，变成一个大语言模型下的向量，也就是用一组固定长度的参数来代表任何一段文本
    """
    positive_review = get_embedding("好评")
    # ILog.debug(__file__, positive_review)
    negative_review = get_embedding("差评")
    positive_example = get_embedding("买的银色版真的很好看，一天就到了，晚上就开始拿起来完系统很丝滑流畅，做工扎实，手感细腻，很精致哦苹果一如既往的好品质")
    negative_example = get_embedding("随意降价，不予价保，服务态度差")

    positive_score = get_score(positive_example)
    negative_score = get_score(negative_example)

    """
    好评通过 Embedding 相似度计算得到的分数是大于 0 的，差评，这个分数是小于 0 的。
    """
    ILog.debug(__file__, "好评例子的评分 : %f" % positive_score)
    ILog.debug(__file__, "差评例子的评分 : %f" % negative_score)

    good_restaurant = get_embedding("这家餐馆太好吃了，一点都不糟糕")
    bad_restaurant = get_embedding("这家餐馆太糟糕了，一点都不好吃")
    good_score = get_score(good_restaurant)
    bad_score = get_score(bad_restaurant)
    ILog.debug(__file__, "好评餐馆的评分 : %f" % good_score)
    ILog.debug(__file__, "差评餐馆的评分 : %f" % bad_score)
