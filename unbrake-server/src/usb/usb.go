package usb

import "github.com/goiiot/libserial"
import "fmt"

type USB struct {
    Connection *libserial.SerialPort
}

func OpenConnection(input string, options ...libserial.Option) *USB {
    connection, err := libserial.Open(input, options...)

    if err != nil{

        fmt.Println(err)
        panic("Connection don't work fine")
    }

    usb := USB{connection}

    return &usb
}
