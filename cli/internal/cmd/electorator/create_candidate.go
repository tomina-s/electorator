package electorator

import (
	"context"
	"fmt"
	"time"

	"github.com/spf13/cobra"
)

const timeFormat = "2 Jan 1999"

func (e *Env) NewCreateCandidateCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "create_candidate",
		Short: "Creates new candidate with given attributes",
		Args: cobra.NoArgs,
	}

	name := cmd.Flags().String("name", "","candidates name")
	party := cmd.Flags().String("party", "", "candidates party")
	info := cmd.Flags().StringP("info", "i", "", "info about candidate")
	photo := cmd.Flags().StringP("photo", "p", "", "candidates photo")
	birthday := cmd.Flags().StringP("birthday", "b", "", "candidates birthday")
	birthplace := cmd.Flags().String("birthplace", "", "candidates birthplace")
	education := cmd.Flags().String("education", "", "candidates education")
	work := cmd.Flags().StringP("work", "w", "", "candidates work")
	position := cmd.Flags().String("position", "", "candidates work")
	politPosition := cmd.Flags().String("polit_position", "", "candidates work")
	_ = cmd.MarkFlagRequired("name")
	_ = cmd.MarkFlagRequired("party")
	_ = cmd.MarkFlagRequired("info")
	_ = cmd.MarkFlagRequired("photo")
	_ = cmd.MarkFlagRequired("birthday")
	_ = cmd.MarkFlagRequired("birthplace")
	_ = cmd.MarkFlagRequired("education")
	_ = cmd.MarkFlagRequired("work")
	_ = cmd.MarkFlagRequired("position")
	_ = cmd.MarkFlagRequired("polit_position")

	cmd.RunE = func(cmd *cobra.Command, args []string) (err error) {
		birth, err := time.Parse(timeFormat, *birthday)
		if err != nil {
			return err
		}
		sql := `INSERT INTO mainapp_candidate (name, party, info, photo, birthday, 
					birthday_place, education, position, polit_position, work) 
			VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)`

		_, err = e.Conn.Exec(context.Background(),
			sql, *name, *party, *info, *photo, birth, *birthplace, *education, *position, *politPosition, *work)
		if err != nil {
			return err
		}

		fmt.Println("Candidate created")
		return
	}

	return cmd
}
