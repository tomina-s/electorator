package ccli

import (
	"encoding/json"
	"fmt"
	"github.com/lensesio/tableprinter"
	"io"

	"bytes"
)

type Printable interface {
	Print() error
}

type Printer struct {
}

func (p *Printer) Print(obj interface{}) error {
	return p.printJSON(obj)
}

func (p *Printer) Sprint(obj interface{}) string {
	var b bytes.Buffer
	printer := tableprinter.New(io.Writer(&b))

	printer.Print(obj)

	return b.String()
}

func (p *Printer) printJSON(obj interface{}) error {
	var data []byte
	var err error
	//if p.pretty {
	//	if data, err = json.MarshalIndent(obj, "", "  "); err != nil {
	//		return err
	//	}
	//
	//	fmt.Println(string(data))
	//	return nil
	//}

	if data, err = json.Marshal(obj); err != nil {
		return err
	}
	fmt.Println(string(data))
	return nil
}
