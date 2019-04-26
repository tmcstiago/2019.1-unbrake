package main

import "fmt"
import "./usb"
import "github.com/goiiot/libserial"

var (
    baseOptions = []libserial.Option{
        libserial.WithDataBits(8),
        libserial.WithParity(libserial.ParityNone),
        libserial.WithHardwareFlowControl(true),
        libserial.WithSoftwareFlowControl(true),
        libserial.WithStopBits(libserial.StopBitOne),
    }
)

func main(){

    fmt.Println("Funcionou")

    teste := usb.OpenConnection("/dev/pts/2", baseOptions...)

    data := make([]byte, 1)

    teste.Connection.Flush()
    for {
       teste.Connection.Read(data[:])
       fmt.Println(data)
    }

    teste.Connection.Close()

}
