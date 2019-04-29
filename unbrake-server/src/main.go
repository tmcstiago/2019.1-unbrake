package main

import "fmt"
import "./usb"
import "github.com/goiiot/libserial"

func main(){

    fmt.Println("Lendo caracteres do terminal")

    teste := usb.OpenConnection(
        "/dev/tty10",
        libserial.WithBaudRate(9600),
        libserial.WithStopBits(libserial.StopBitOne))

    teste.Connection.Flush()

    data := make([]byte, 1)

    teste.Connection.Flush()
    for {
       teste.Connection.Read(data[:])
       fmt.Printf("%s\n", data)
    }

    teste.Connection.Close()

}
