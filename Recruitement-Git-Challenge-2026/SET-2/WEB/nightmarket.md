

### **Chrome Junkie - Quick Write-Up**

* **Goal:** Bypass user restrictions to buy a VIP item and get the flag.
* **Step 1:** Found the `session_data` cookie in browser storage, which used Base64-encoded JSON (`{"balance": 50000, "tier": "standard"}`).
* **Step 2:** Decoded it, changed the values to give ourselves admin/VIP privileges and unlimited funds (`{"balance": 999999, "tier": "vip"}`), and re-encoded it back to Base64.
* **Step 3:** Replaced the old cookie value with the new Base64 string and refreshed the page to unlock the VIP black market items.
* **Step 4:** Clicked **BUY NOW** on the restricted item to complete the transaction and reveal the flag.

#### **Flag**

`bi0s{3dd13s_4r3_just_numb3rs_0n_4_scr33n}` 