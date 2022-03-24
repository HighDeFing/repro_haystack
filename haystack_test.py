from haystack_upload_files import Haystack_module

if __name__ == "__main__":
    elastic = Haystack_module()
    elastic.init_QAPipeline()
    elastic_pipe = elastic.get_QAPipeline()
    query = '¿Qué es un adolescente?'
    result = elastic_pipe.run(query=query, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 3}})
    print(result)