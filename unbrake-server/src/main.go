package main

import "fmt"
import "./usb"

func main(){

    fmt.Println("Funcionou")

    teste := usb.OpenConnection("/dev/pts/1")

    data := make([]byte, 1)

    teste.Connection.Flush()
    value, _ := teste.Connection.Read(data[:])

    fmt.Println(data)
    fmt.Println(value)

    teste.Connection.Close()

}
