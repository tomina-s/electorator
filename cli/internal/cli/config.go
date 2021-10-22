package ccli

import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/mitchellh/go-homedir"
)

func GetConfigPath(configFile string) (string, error) {
	if configFile != "" {
		_, err := os.Stat(configFile)
		if err != nil {
			return "", err
		}

		return configFile, nil
	}

	home, err := homedir.Dir()
	if err != nil {
		return "", err
	}
	homeConfigFile := filepath.Join(home, ".cli")
	_, err = os.Stat(homeConfigFile)
	if err == nil {
		return homeConfigFile, nil
	}

	etcConfigFile := "/etc/cli/config.yaml"
	_, err = os.Stat(etcConfigFile)
	if err == nil {
		return etcConfigFile, nil
	}

	return "", fmt.Errorf("config file not found in default locations: %s, %s", homeConfigFile, etcConfigFile)
}
