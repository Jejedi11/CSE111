import math

item_total = int(input("How many items will be manufactured? "))
item_per_box = int(input("How many items will a single box hold? "))

reqd_boxes = math.ceil(item_total / item_per_box)

print(f"For {item_total} items, packing {item_per_box} items per box, you will need {reqd_boxes} boxes.")