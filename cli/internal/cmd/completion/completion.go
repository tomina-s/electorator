package completion

import (
	"os"

	"github.com/spf13/cobra"
)

// completionCmd represents the completion command
func New() *cobra.Command {
	cmd := &cobra.Command{
		Hidden: true,
		Use:    "completion [bash|zsh|fish|powershell]",
		Short:  "Generate completion script",
		Long: `To load completions:
	
	Bash:
	
	  $ source <(cli completion bash)
	
	  # To load completions for each session, execute once:
	  # Linux:
	  $ cli completion bash > /etc/bash_completion.d/cli
	  # macOS:
	  $ cli completion bash > /usr/local/etc/bash_completion.d/cli
	
	Zsh:
	
	  # If shell completion is not already enabled in your environment,
	  # you will need to enable it.  You can execute the following once:
	
	  $ echo "autoload -U compinit; compinit" >> ~/.zshrc
	
	  # To load completions for each session, execute once:
	  $ cli completion zsh > "${fpath[1]}/_cli"
	
	  # You will need to start a new shell for this setup to take effect.
	
	fish:
	
	  $ cli completion fish | source
	
	  # To load completions for each session, execute once:
	  $ cli completion fish > ~/.config/fish/completions/cli.fish
	
	PowerShell:
	
	  PS> cli completion powershell | Out-String | Invoke-Expression
	
	  # To load completions for every new session, run:
	  PS> cli completion powershell > cli.ps1
	  # and source this file from your PowerShell profile.
	`,
		DisableFlagsInUseLine: true,
		ValidArgs:             []string{"bash", "zsh", "fish", "powershell"},
		Args:                  cobra.ExactValidArgs(1),
		// hack to disable persistent required 'environment' flag
		PersistentPreRunE: func(cmd *cobra.Command, args []string) error {
			flags := cmd.InheritedFlags()
			_ = flags.SetAnnotation("environment", cobra.BashCompOneRequiredFlag, []string{"unknown"})
			return nil
		},
		// end hack
		Run: func(cmd *cobra.Command, args []string) {
			switch args[0] {
			case "bash":
				_ = cmd.Root().GenBashCompletion(os.Stdout)
			case "zsh":
				_ = cmd.Root().GenZshCompletion(os.Stdout)
			case "fish":
				_ = cmd.Root().GenFishCompletion(os.Stdout, true)
			case "powershell":
				_ = cmd.Root().GenPowerShellCompletionWithDesc(os.Stdout)
			}
		},
	}

	return cmd
}
