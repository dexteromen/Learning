package main

import ("fmt"
)

func main(){
	var n int 
	fmt.Println("enter n:")
	fmt.Scan(&n)
	isPrime := true
	if n<=1{
		isPrime = false
	}else{
		for i := 2; i*i <=n; i++ {
			if n%i == 0{
				isPrime =false
				break
			}
		}
	}

	if isPrime {
		fmt.Println(n," is Prime")
	}else{
		fmt.Println(n, " is not prime.")
	}
}