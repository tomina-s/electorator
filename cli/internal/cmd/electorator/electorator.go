package electorator

import (
	"context"
	cli "electorator/cli/internal/cli"
	"fmt"

	"github.com/jackc/pgx/v4/pgxpool"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

const dsn = `pool_max_conns=1 host=%s port=%s user=%s password=%s dbname=%s sslmode=disable`

type DB struct {
	Host string
	Port string
	User string
	Password string
	Name string
}

type Conf struct {
	Db DB
}

type Env struct {
	Conf *Conf
	Conn *pgxpool.Pool
	Printer *cli.Printer
}

func New(env *Env) *cobra.Command {
	cmd := &cobra.Command{
		Use:   "admin",
		Short: "User admin tools",
		Long:  `Admin tools`,
	}

	cmd.PersistentPreRunE = func(cmd *cobra.Command, args []string) error {
		if err := cmd.Root().PersistentPreRunE(cmd, args); err != nil {
			return err
		}

		environment := viper.GetString("environment")

		if err := viper.UnmarshalKey(environment, &env.Conf); err != nil {
			return err
		}

		dsnFmt := fmt.Sprintf(dsn, env.Conf.Db.Host, env.Conf.Db.Port,
			env.Conf.Db.User, env.Conf.Db.Password, env.Conf.Db.Name)

		config, err := pgxpool.ParseConfig(dsnFmt)
		if err != nil {
			return err
		}

		env.Conn, err = pgxpool.ConnectConfig(context.Background(), config)

		return err
	}

	cmd.AddCommand(env.NewCreateUserCmd())

	return cmd
}
