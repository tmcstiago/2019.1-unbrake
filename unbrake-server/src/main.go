package main

import "fmt"
import "./usb"

func main(){

    fmt.Println("Funcionou")

    teste := usb.OpenConnection("/dev/pts/2")

    data := make([]byte, 1)

    teste.Connection.Flush()
    for {
       teste.Connection.Read(data[:])
       fmt.Println(data)
    }

    teste.Connection.Close()

}
