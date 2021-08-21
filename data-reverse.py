  """
11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
 
 should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
 """

def data_reverse(data):
  res = []
  
  for i in range(len(data)-8, -1, -8):
    res.extend(data[i:i+8])
  
  return res
