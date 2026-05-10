from langchain_community.vectorstores import Chroma

import config_data as config

class VectorStoreService(object):
    def __init__(self,embedding):
        """
        param embedding: embedding model 嵌入模型
        """

        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=embedding,
            persist_directory=config.persist_directory,
                     
        )

    def get_retriever(self):
        # 返回向量数据库检索器,方便加入chain
        return self.vector_store.as_retriever(search_kwargs={"k":config.similarity_threshod})
    

if __name__ == "__main__":
    from langchain_community.vectorstores import Chroma
    from langchain_community.embeddings import DashScopeEmbeddings
    embedding = DashScopeEmbeddings(model="text-embedding-v4")
    vector_store = VectorStoreService(embedding)
    retriever = vector_store.get_retriever()
    res = retriever.invoke("我的体重是180斤,尺码推荐")
    print(res)