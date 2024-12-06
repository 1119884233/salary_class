from py2neo import Graph
from config import config

#  链接Neo4j数据库
def connect_to_neo4j():
    #  链接Neo4j数据库
    graph_neo4j = Graph('bolt://localhost:7687', auth=(config.neo4j_user,config.neo4j_password))
    return graph_neo4j

#  创建工作种类节点
def create_job_type_node(job_name):
    #  定义Cypher语言，创建工作种类节点
    create_job_type_node = "CREATE (job_type:job_type{name:'"+str(job_name)+"'})"
    return create_job_type_node

#  创建节点和关系
def create_node_and_relationship(job_name,jon_info):

    #  定义Cypher语言，创建每个工作种类的具体工作
    create_job_info_node = "CREATE (job_name:job_name{job_name:'"+jon_info+"'})"

    #  定义Cypher语言，用来创建两者之间的关系
    create_relationship = "match (job_type:job_type{name:'"+job_name+"'}),(job_name:job_name{job_name:'"+jon_info+"'}) MERGE (job_type)-[:job_info]->(job_name)"

    #  返回三个Cypher语言
    return create_job_info_node,create_relationship


