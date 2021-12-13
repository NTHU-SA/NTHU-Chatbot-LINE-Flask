workers = 4    # 定義同時開啟的處理請求的進程數量，根據網站流量適當調整
preload = True
worker_class = "gevent"   # 採用gevent，支持亦不處理請求，提高吞吐量
bind = "0.0.0.0:5000"    # 監聽IP放寬、以便於Docker之間、Docker和宿主機之間的通信