package electorator

import (
	"context"
	"fmt"

	"github.com/spf13/cobra"
)

func (e *Env) NewClearDbCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "clear",
		Short: "Creates new user with given name and password",
		Args: cobra.NoArgs,
	}

	all := cmd.Flags().BoolP("all", "a", false, "clear all elections tables")
	user := cmd.Flags().BoolP("user", "u", false, "clear user tables")

	cmd.RunE = func(cmd *cobra.Command, args []string) (err error) {
		sqlTrunc := `truncate mainapp_tik, mainapp_uikprotocol1, mainapp_protocol1, mainapp_protocol2`
		sqlSeq := `SELECT setval('mainapp_protocol1_id_seq', 1),
		   setval('mainapp_protocol2_id_seq', 1),
		   setval('mainapp_tik_id_seq', 1),
		   setval('mainapp_uikprotocol1_id_seq', 1)`
		if *all {
			sqlTrunc += ", accounts_permission, mainapp_uikcandidate, mainapp_uik, mainapp_candidate"
			sqlSeq += `, setval('mainapp_uik_id_seq', 1),
				setval('mainapp_candidate_id_seq', 1),
				setval('mainapp_uikcandidate_id_seq', 1),
				setval('accounts_permission_id_seq', 1)`
		}
		if *user {
			sqlTrunc += ", accounts_role, accounts_permission, accounts_account"
			sqlSeq += `, setval('accounts_account_id_seq', 1),
				setval('accounts_role_id_seq', 1),
				setval('accounts_permission_id_seq', 1)`
		}
		sqlTrunc += " cascade"

		_, err = e.Conn.Exec(context.Background(), sqlTrunc)
		if err != nil {
			return err
		}

		_, err = e.Conn.Exec(context.Background(), sqlSeq)
		if err != nil {
			return err
		}

		fmt.Println("Database cleared")
		return
	}

	return cmd
}
