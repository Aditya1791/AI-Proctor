import cv2
import os
import sys

print('--- STARTING EXAM BIOMETRIC DEEPFACE MODEL TEST INSIDE CONTAINER ---')
try:
    from deepface import DeepFace
    print('SUCCESS: DeepFace package is installed and imported correctly.')
except Exception as e:
    print('ERROR: DeepFace is not installed or failed to import:', e)
    sys.exit(1)

# Paths to student photos inside container
image_path1 = 'static/Aditya_Prasad_Panda.jpeg'
image_path2 = 'static/Abhishek_Rana.jpg'

if os.path.exists(image_path1) and os.path.exists(image_path2):
    print('Real-world student images found in static folder inside container.')
    
    # Let's perform self-verification (should be True)
    print('\n[TEST 1] Verifying Aditya Panda against himself (expected result: Verified)...')
    try:
        img1 = cv2.imread(image_path1)
        res_self = DeepFace.verify(img1, img1, enforce_detection=False)
        print('SUCCESS: Inference completed.')
        print('  Verified:', res_self.get('verified'))
        print('  Cosine Distance:', res_self.get('distance'))
        print('  Model used:', res_self.get('model'))
    except Exception as e:
         print('ERROR during self-verification:', e)
         
    # Let's perform cross-verification (should be False)
    print('\n[TEST 2] Verifying Aditya Panda against Abhishek Rana (expected result: NOT Verified)...')
    try:
        img2 = cv2.imread(image_path2)
        res_cross = DeepFace.verify(img1, img2, enforce_detection=False)
        print('SUCCESS: Inference completed.')
        print('  Verified:', res_cross.get('verified'))
        print('  Cosine Distance:', res_cross.get('distance'))
        print('  Model used:', res_cross.get('model'))
    except Exception as e:
         print('ERROR during cross-verification:', e)
         
else:
    print('ERROR: Test images not found in static folder inside container.')
