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
	role := cmd.Flags().StringP("role", "r", "УИК", "role for new user")
	name := cmd.Flags().StringP("name", "n", "", "full name of the user")
	permissions := cmd.Flags().IntSliceP("permissions", "p", []int{}, "full name of the user")
	_ = cmd.MarkFlagRequired("username")
	_ = cmd.MarkFlagRequired("password")
	_ = cmd.MarkFlagRequired("role")
	_ = cmd.MarkFlagRequired("name")

	cmd.RunE = func(cmd *cobra.Command, args []string) (err error) {
		if *role == "МГИК" {
			*role = "ЦИК"
		}
		hash, err := unchained.MakePassword(*password, *username, "pbkdf2_sha256")
		if err != nil {
			return err
		}

		sql := `INSERT INTO accounts_account (password, name, username) 
			VALUES ($1, $2, $3) 
			RETURNING id`

		var id int
		err = e.Conn.QueryRow(context.Background(),
			sql, hash, name, username).Scan(&id)
		if err != nil {
			return err
		}

		sql = `INSERT INTO accounts_role (user_id, role_user) 
			VALUES ($1, $2) 
			ON CONFLICT 
			DO NOTHING`

		_, err = e.Conn.Exec(context.Background(),
			sql, id, *role)
		if err != nil {
			return err
		}

		sql = `INSERT INTO accounts_permission (user_id, uik_id) 
			VALUES ($1, $2) 
			ON CONFLICT 
			DO NOTHING`
		for _, p := range *permissions {
			_, err = e.Conn.Exec(context.Background(),
				sql, id, p)
			if err != nil {
				return err
			}
		}

		fmt.Println("User created")
		return
	}

	return cmd
}
