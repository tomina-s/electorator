package main

import (
	"electorator/cli/internal/cmd/completion"
	"fmt"
	"os"

	log "github.com/sirupsen/logrus"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"

	cli "electorator/cli/internal/cli"
)

func main() {
	cmd := &cobra.Command{
		Use:           "cli",
		Short:         "Command line interface",
		Long:          "Command line interface",
		SilenceErrors: true,
		SilenceUsage:  true,
	}

	configFile := cmd.PersistentFlags().StringP("config", "c", "", "Config file (default is ~/.ccli, then /etc/cli/config.yaml)")

	cmd.PersistentFlags().StringP("environment", "e", "", "Current environment (prod,dev,...) (required)")
	_ = viper.BindPFlag("environment", cmd.PersistentFlags().Lookup("environment"))

	cmd.PersistentPreRunE = func(cmd *cobra.Command, args []string) error {
		cfg, err := cli.GetConfigPath(*configFile)
		if err != nil {
			return err
		}

		log.Infof("Start using config %s", cfg)

		viper.SetConfigType("yaml")
		viper.SetConfigFile(cfg)

		if err := viper.ReadInConfig(); err != nil {
			return err
		}

		environment := viper.GetString("environment")
		if environment == "" {
			return fmt.Errorf("set environment in -e flag or [environment] config file")
		}

		if viper.Get(environment) == nil {
			return fmt.Errorf("environment %s  not found in config", environment)
		}
		log.Infof("Start using environment %s", environment)

		return nil
	}

	cmd.AddCommand(completion.New())

	if err := cmd.Execute(); err != nil {
		_, _ = fmt.Print(err)
		os.Exit(1)
	}
}
