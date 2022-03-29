# Comece executando as instruções de atribuição:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
# Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
# (a) 'ant bat cod'
s1 + ' ' + s2 + ' ' + s3

# (b) 'ant ant ant ant ant ant ant ant ant ant'
9 * (s1 + ' ') + s1
# (c) 'ant bat bat cod cod cod'
s1 + ' ' + 2 * (s2 + ' ') + 2 * (s3 + ' ') + s3

# (d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
6 * (s1 + ' ' + s2 + ' ') + s1 + ' ' + s2

# (e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
4 * (2 * (s2) + s3 + ' ') + 2 * (s2) + s3