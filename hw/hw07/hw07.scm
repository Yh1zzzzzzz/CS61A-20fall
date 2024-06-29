(define (filter-lst fn lst) 'YOUR-CODE-HERE
   (if (null? lst)  '()     (if (fn  (car lst) )  (cons (car lst) (filter-lst fn  (cdr lst) ) )  (filter-lst  fn (cdr lst))
        )





    )
    
)
    
    

; ;; Tests
(define (even? x) (= (modulo x 2) 0))

(filter-lst even? '(0 1 1 2 3 5 8))

; expect (0 2 8)
(define (interleave first second) 'YOUR-CODE-HERE
  (if   (null? first) second  (if  (null? second) first  (cons (car first)  (interleave   second    (cdr first)  )   )    ))

)

(interleave (list 1 3 5) (list 2 4 6))

; expect (1 2 3 4 5 6)
(interleave (list 1 3 5) nil)

; expect (1 3 5)
(interleave (list 1 3 5) (list 2 4))

; expect (1 2 3 4 5)
(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (if (= n 0) start (combiner (term n) (accumulate combiner start (- n 1)term)))
  )

(define (no-repeats lst) 'YOUR-CODE-HEREk
  (define (helper n lst)
    (if (null? lst) #t (if (= n (car lst)) #f  (helper n (cdr lst)) ))
    (if (helper  (car lst) (cdr lst) )  (cons (car lst)  (no-repeats (cdr lst)))  (no-repeats (cdr lst))  )
  
  )



)
