package main
import "fmt"
import "./usb"
import "strconv"
import "github.com/goiiot/libserial"


var (
	baseOptions = []libserial.Option{
		libserial.WithDataBits(8),
		libserial.WithParity(libserial.ParityNone),
		libserial.WithHardwareFlowControl(true),
		libserial.WithSoftwareFlowControl(true),
	}
)


func main(){

    fmt.Println("Funcionou")

    teste := usb.OpenConnection("/dev/pts/1", baseOptions...)

    fmt.Println([]byte(strconv.Itoa(10)))
    value2, err2 := teste.Connection.Write([]byte("asdf"))


    teste.Connection.Close()

    if err2 != nil{
        panic(err2)
    }

    fmt.Println(value2)

}
