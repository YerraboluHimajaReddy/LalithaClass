pow2 = [2 ** x for x in range(12)]
print(pow2) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512], [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]


#2nd way
pow2 = []
for x in range(10):
   pow2.append(2 ** x)

   print(pow2)

   #[1]
   #[1, 2]
   #[1, 2, 4]
   #[1, 2, 4, 8]
   #[1, 2, 4, 8, 16]
   #[1, 2, 4, 8, 16, 32]
   #[1, 2, 4, 8, 16, 32, 64]
   #[1, 2, 4, 8, 16, 32, 64, 128]
   #[1, 2, 4, 8, 16, 32, 64, 128, 256]
   #[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

   pow2 = [2 ** x for x in range(10) if x > 5]
   print(pow2) # [64, 128, 256, 512, 512]

   print("=======================")
   my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
   print('p' in my_list) # True
   print('z' in my_list) # False

