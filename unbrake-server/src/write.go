package main
import "fmt"
import "./usb"
import "strconv"

func main(){

    fmt.Println("Funcionou")

    teste := usb.OpenConnection("/dev/pts/2")

    fmt.Println([]byte(strconv.Itoa(10)))
    teste.Connection.Write([]byte(" "))

    teste.Connection.Close()

}
