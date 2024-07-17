import {Config} from '../affected';

export const python = new Config({
  match: ['**'],
  ignore: ['**/README.md'],
  packageConfig: [
    'noxfile_config.py',
    'requirements.txt',
    'pyproject.toml',
    'setup.py',
    'setup.cfg',
  ],
});