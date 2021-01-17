import math

#key返却関数
def get_key_value(cost, processed_node):
    return [k for k, v in cost.items() if v == processed_node]

#　コストが小さいKeyを算出する関数
def get_taget_node(cost, prev):
    target_list = list(cost.keys())
    for i in prev:
        target_list.remove(i)
    #現在のコスト
    now_cost = cost[target_list[0]]
    for key in target_list[1:]:
        now_cost = min([now_cost, cost[key]])
    return get_key_value(cost, now_cost)

# ダイクストラ法のアルゴリズム
def dijkstras(graph):
    # 変数用意
    processed_node = [] #処理完了ノード格納用
    prev_node = {} #直前のノード格納用
    cost = {} #コスト格納用

    for key in graph.keys():
        prev_node[key] = "" 
        cost[key] = math.inf #各ノードの初期化

    #スタート位置設定
    for i in graph['S'].keys():
        cost[i] = graph['S'][i]
        prev_node[i] = 'S'

    #処理完了ノードがある場合は続行探索を続行
    while len(processed_node) < len(graph.keys()):
        #costの中で一番コストの低いノードを取り出す
        tmp = get_taget_node(cost,processed_node)
        for node in tmp:
            #移動可能なノードの処理
            for key in graph[node].keys():
                #前回のコストのほうが小さければ更新
                if cost[key] > cost[node] + graph[node][key]:
                    cost[key] = cost[node] + graph[node][key]
                    prev_node[key] = node

            processed_node.append(node)
    return cost, prev_node

#最短経路算出関数
def short_root(prev):
    root = ['G']
    now = 'G'
    while now != 'S':
        root.append(prev[now])
        now = prev[now]
    return root[::-1]

if __name__ == "__main__":
    #初期化
    graph = {}
    S, A, B, C, G = {}, {}, {}, {}, {}
    S['A'] = 5
    S['B'] = 10
    A['C'] = 3
    A['B'] = 2
    B['A'] = 2
    B['C'] = 4
    B['G'] = 2
    C['G'] = 3

    graph['S'] = S
    graph['A'] = A
    graph['B'] = B
    graph['C'] = C
    graph['G'] = G

    cost,prev_node = dijkstras(graph)
    print('ゴールまでのコスト:', cost['G'])
    print('最短経路:', short_root(prev_node))