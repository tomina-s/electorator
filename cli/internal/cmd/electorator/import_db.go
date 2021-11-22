package electorator

import (
	"fmt"
	"os/exec"

	"github.com/spf13/cobra"
)

func (e *Env) NewImportDbCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "import",
		Short: "Import data from file",
		Args: cobra.NoArgs,
	}

	file := cmd.Flags().StringP("file", "f", "./dump.sql", "path to dump file")

	cmd.RunE = func(cmd *cobra.Command, args []string) (err error) {

		params := []string{"-U", e.Conf.Db.User, "-h", e.Conf.Db.Host, "-p", e.Conf.Db.Port,
			"-d", e.Conf.Db.Name, "-f", *file}
		p := exec.Command("psql", params...)

		out, err := p.Output()
		if err != nil {
			return err
		}

		fmt.Println(string(out))
		fmt.Println("DB dump created")
		return
	}

	return cmd
}
