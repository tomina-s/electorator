package electorator

import (
	"fmt"
	"os"
	"os/exec"

	"github.com/spf13/cobra"
)

func (e *Env) NewDumpDbCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "dump",
		Short: "Creates dump file",
		Args: cobra.NoArgs,
	}

	file := cmd.Flags().StringP("file", "f", "./dump.sql", "path to dump file")

	cmd.RunE = func(cmd *cobra.Command, args []string) (err error) {

		params := []string{"-U", e.Conf.Db.User, "-h", e.Conf.Db.Host, "-p", e.Conf.Db.Port,
			"--column-inserts", "--data-only", e.Conf.Db.Name}
		p := exec.Command("pg_dump", params...)

		outfile, err := os.Create(*file)
		if err != nil {
			return err
		}
		defer outfile.Close()

		p.Stdout = outfile
		err = p.Start()
		if err != nil {
			return err
		}

		fmt.Println("DB dump created")
		return
	}

	return cmd
}
