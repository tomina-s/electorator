package electorator

import (
	"context"
	"fmt"

	"github.com/spf13/cobra"
)

func (e *Env) NewCreateUikCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "create_uik",
		Short: "Creates new uik with given attributes",
		Args: cobra.NoArgs,
	}

	numUik := cmd.Flags().IntP("number", "n", 0,"uik number")
	population := cmd.Flags().IntP("population", "p", 0, "population")
	numTik := cmd.Flags().String("tik", "ТИК", "tik that uik belongs to")
	_ = cmd.MarkFlagRequired("num_uik")
	_ = cmd.MarkFlagRequired("population")
	_ = cmd.MarkFlagRequired("num_tik")

	cmd.RunE = func(cmd *cobra.Command, args []string) (err error) {
		sql := `INSERT INTO mainapp_uik (num_uik, population, num_tik, status, sum_votes, 
					sum_numb_votes_fin, presence, perc_final_bul, bad_form, update_time) 
			VALUES ($1, $2, $3, false, 0, 0, 0, 0, 0, current_timestamp)`

		_, err = e.Conn.Exec(context.Background(),
			sql, *numUik, *population, *numTik)
		if err != nil {
			return err
		}

		fmt.Println("Uik created")
		return
	}

	return cmd
}
