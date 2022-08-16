import html_creater as hc
import xml_generator as xg
import data_provider as dp

# print(hc.create())  # логирование в файл log.csv, если снизу отключить 6 и 8 пункт
# print(xg.create())

hc.new_create(xg.new_create(dp.data_collection()))