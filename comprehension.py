healthy = ["Apple", "Orenge", "Benana"]
buckets = ["Pizza", "Canvas", "Orenge"]

healthy_backpack = []

for item in buckets:
    if item in healthy:
          healthy_backpack.append(item.upper())

print(healthy_backpack)