# [LUCAS AMRHEIN] - Assignment 2

def evaluate_packet(port, packet_size_bytes):
   if port in (80, 443):
       return 'STANDARD_WEB_TRAFFIC'
   elif packet_size_bytes > 1500:
       return 'SUSPICIOUS_LARGE_PACKET'
   elif packet_size_bytes < 64:
       return 'SUSPICIOUS_SMALL_PACKET'
   else:
       return 'NORMAL_INTERNAL_TRAFFIC'