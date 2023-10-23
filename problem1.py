##### Problem 1
"""
H a v e t h e u s e r e n t e r a u s e r n a m e a n d p a s s w o r d .
R e p e a t t h i s u n t i l b o t h t h e u s e r n a m e a n d p a s s w o r d m a t c h t h e 
f o l l o w i n g :
u s e r n a m e : a d m i n
p a s s w o r d : 1 2 3 4 5
I f t h e y g u e s s m o r e t h a n 3 t i m e s , t h e y a r e n o t a l l o w e d t o g u e s s
a n y m o r e a n d t h e p r o g r a m w i l l e n d .
( 2 m a r k s )

i n p u t s :
s t r u s e r n a m e
s t r p a s s w o r d

o u t p u t s :
A c c e s s g r a n t e d
A c c e s s d e n i e d

e x a m p l e :
e x a m p l e :
E n t e r u s e r n a m e : f r e d
E n t e r p a s s w o r d : p a s s w o r d
A c c e s s d e n i e d
E n t e r u s e r n a m e : a d m i n
E n t e r p a s s w o r d : p a s s w o r d
A c c e s s d e n i e d
E n t e r u s e r n a m e : a d m i n
E n t e r p a s s w o r d : 1 2 3 4
A c c e s s d e n i e d
T o o m a n y f a i l e d a t t e m p t s . A c c e s s d e n i e d .
"""

username = ""
password = ""
tries = 3
while username != "admin" and password != "12345":
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username != "admin" and password != "12345":
        print("Access Denied")
        tries = tries - 1
        if tries == 0: 
            print("Too many failed atempts. Access Denied")
            break
    else:
        print("Access Granted")

