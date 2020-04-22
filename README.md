# Balanced: A time management service.

## Requirements
- Python3
- NodeJS

## Quickstart
```bash
git clone https://github.com/aDotInTheVoid/balanced_omni
cd balanced_omni/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements-dev.txt
yarn install # This mat take some time.
./manage.py migrate
./manage.py createsuperuser # Follow prompts
./manage.py runserver & yarn serve && fg
```

The dev server is now running. To stop it first type ^C. This will stop the frontend server. To stop the backend enter `fg` to put it into the forground and then ^C it.

## Project tools
- `yarn serve`: run the dev server.
- `yarn serve:dist`: server the generated files. Faster performance but no Hot reload or sourcemaps. Good for demos
- `yarn build`: Build the frontend to the `dist` directory for deployment or demos.
- `yarn test:unit`/`yarn test:e2e`: Run unit or e2e test. Currently not implemented
- `yarn test:e2e --headless`: Run e2e tests in headless mode.
- `./manage.py test`: Run backend tests
- `yarn lint`: Run frontend linter and backend checker
- `yarn lintpy`: Run backend linter
- `yarn fmt`: Format frontend and backend
- `yarn fmtpy`: Format backend
- `yarn pycov`: Run coverage on the backend

## Contributing
Contributitions, either in the form of pull requests or issues are welcome. 


---

## Notes for me
### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
### Notes
- [Backend ref](https://github.com/howardderekl/conduit-django)
- [DRF stuffs](https://github.com/beda-software/drf-writable-nested)
- [Azure Balance](https://www.microsoftazuresponsorships.com/Balance)
