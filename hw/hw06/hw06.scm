(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cdr (cdr s)))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond
    ((> num 0  ) 1)
    ((= num 0)  0)
    (else -1)
  )
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  (cond
    ((= y 1) x)
    ((= y 0) 1)
    ((even? y) (pow (square x) (/ y 2)  )    )
    ((odd? y ) (* x (pow x (- y 1)) )   )
    (else 'error)
  )
)

