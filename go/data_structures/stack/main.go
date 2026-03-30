package main

import (
	"errors"
	"fmt"
)

// type Stack[T comparable] []T
type Stack[T any] []T

func (s *Stack[T]) Empty() bool {
	return len(*s) == 0
}

func (s *Stack[T]) Length() int {
	return len(*s)
}

func (s *Stack[T]) Pop() (T, error) {
	if s.Empty() {
		var zero T
		return zero, errors.New("StackEmpty")
	}
	v := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return v, nil
}

func (s *Stack[T]) Push(v T) {
	*s = append(*s, v)
}

func main() {
	intStack := &Stack[int]{}
	fmt.Println("s", intStack)
	intStack.Push(5)
	fmt.Println("s", intStack)
	fmt.Println("len", intStack.Length())
	v, err := intStack.Pop()
	fmt.Printf("v=%d, err=%v\n", v, err)
	v, err = intStack.Pop()
	fmt.Printf("v=%d, err=%v\n", v, err)

	fmt.Println()

	stringStack := &Stack[string]{}
	fmt.Println("s", stringStack)
	stringStack.Push("i")
	fmt.Println("s", stringStack)
	stringStack.Push("am")
	fmt.Println("s", stringStack)
	stringStack.Push("BT")
	fmt.Println("s", stringStack)
	fmt.Println("len", stringStack.Length())
}
