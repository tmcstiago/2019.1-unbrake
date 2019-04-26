package main
import "fmt"
import "./usb"
import "github.com/goiiot/libserial"
import "strconv"


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

    fmt.Println([]byte(strconv.Itoa(10)))

    for i:=0; i < 256; i++{
        teste.Connection.Write([]byte(strconv.Itoa(i)))
    }
    teste.Connection.Close()

}
