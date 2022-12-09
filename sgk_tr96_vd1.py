raw_secs = int(input("Nhập giây: "))
d = raw_secs // 86400
d_left = raw_secs % 86400
h = d_left // 3600
h_left = d_left % 3600
m = h_left // 60
s = h_left % 60
print(d,"d ",h,"h ",m,"m ",s,"s ",sep="") 
