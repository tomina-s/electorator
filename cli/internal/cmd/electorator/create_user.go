package electorator

import (
	"context"
	"fmt"

	"github.com/alexandrevicenzi/unchained"
	"github.com/spf13/cobra"
)

func (e *Env) NewCreateUserCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "create_user",
		Short: "Creates new user with given name and password",
		Args: cobra.NoArgs,
	}

	username := cmd.Flags().String("username", "", "short name for new user to login")
	password := cmd.Flags().String("password", "", "password for new user to login")
	name := cmd.Flags().String("name", "", "full name of the user")
	_ = cmd.MarkFlagRequired("username")
	_ = cmd.MarkFlagRequired("password")
	_ = cmd.MarkFlagRequired("name")

	cmd.RunE = func(cmd *cobra.Command, args []string) (err error) {
		hash, err := unchained.MakePassword(*password, *username, "pbkdf2_sha256")
		if err != nil {
			return err
		}

		sql := `INSERT INTO accounts_account (password, name, username) 
			VALUES ($1, $2, $3)
			ON CONFLICT 
			DO NOTHING`

		_, err = e.Conn.Exec(context.Background(),
			sql, hash, name, username)


		if err != nil {
			return err
		}

		fmt.Println("User created")
		return
	}

	return cmd
}
