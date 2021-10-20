package ccli

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func Confirmation() bool {
	reader := bufio.NewReader(os.Stdin)
	for {
		s, _ := reader.ReadString('\n')
		s = strings.TrimSuffix(s, "\n")
		s = strings.ToLower(s)
		if len(s) > 1 {
			fmt.Fprintln(os.Stderr, "Please enter Y or N")
			continue
		}
		if strings.EqualFold(s, "n") {
			return false
		} else if strings.EqualFold(s, "y") {
			break
		} else {
			continue
		}
	}
	return true
}
