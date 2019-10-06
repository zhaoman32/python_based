import json
# 获得两个字母的国别码
import pygal.maps.world  # 导入世界地图包pygal_maps_world

# 定义函数，返回适用于pygal的两位国别码
def get_country_code(country_name):
     # pygal两位国别码列表表示法：pygal.maps.world.COUNTRIES.items()
    for code,name in pygal.maps.world.COUNTRIES.items():
        if name == country_name:
            return code
    return None

# ------------------------
filename = 'population_json.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}   # 用于存储人口数据
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            print(code + ": " + str(population))
        else:
            print("ERROR - " + country_name)



#根据人口数量将国家分成三组，0-1千万，1千万-10亿，10亿以上
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm = pygal.maps.world.World()                        # 生成世界地图实例
wm.title = 'World Population in 2010, by Country'    # 设置标题
wm.add('1-10m',cc_pops_1)                            # 添加0——1千万的国家和人口
wm.add('10m-1bn',cc_pops_2)                          # 添加1千万——10亿的国家和人口
wm.add('>bn',cc_pops_3)                              # 添加10亿以上的国家和人口
wm.render_to_file('world_population.svg')            # 渲染视图到文件，通过浏览器可查看





