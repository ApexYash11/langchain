# LangChain — Learning Journal and Project Notes

This repository documents my practical learning and experiments with LangChain and related tools. Below you'll find a clear overview of what I learned, what I implemented in this repo, how I ran examples, known issues I fixed, and next steps I planned.

## What I learned
- LangChain core concepts: LLMs, prompts, prompt templates, chains, and runnables, and how these compose into applications.
- How to design `PromptTemplate` instances and pass matching input variables to `invoke` to avoid KeyErrors.
- How to compose prompts and models into pipelines using the `|` operator and runnables.
- How agents and tools can be used to orchestrate external actions (APIs, searches, etc.).
- Document ingestion using `TextLoader`, `PyPDFLoader`, and `WebBaseLoader`, and handling common loader issues.
- Text chunking strategies with `RecursiveCharacterTextSplitter` (chunk size, overlap), and adapting code to API signature changes.
- Using output parsers (`StrOutputParser`, `PydanticOutputParser`) to structure and validate model outputs.
- Provider-specific model integrations (e.g., `ChatGoogleGenerativeAI`) and environment-driven configuration.
- Dependency and version management for `langchain`, `langchain-core`, and `langchain-community`.

## What I implemented (folder-by-folder)

- `chatmodel/`
	- Implementations demonstrating how to configure chat-capable models and compose prompts into multi-step chains.
	- Files: `chatmodel_hf.py`, `chatmodel_anthropic.py`, `chatmodel.py`.

- `document-loaders/`
	- Examples for loading and summarizing documents.
	- `txt.py`: loads a local `poem.txt`, builds a prompt template that expects `poem`, chains prompt → model → parser, and prints the result.
	- `webloader.py`: loads content from a URL using `WebBaseLoader`; the script sets a `USER_AGENT` to avoid request blocking.
	- PDF loader experiments using `PyPDFLoader` (I used corrected file paths where needed).

- `textsplitter/` (text splitter experiments)
	- Demonstrations of `RecursiveCharacterTextSplitter`.
	- Files (renamed to avoid shadowing built-ins): `split_by_string_demo.py` (was `str.py`), `split_document_demo.py` (was `doc.py`), `split_by_length_demo.py` (was `len.py`).
	- Learning: chunk size and overlap tuning, and removing unsupported constructor arguments to match the installed package version.

- `llm/`
	- `llm_demo.py`: small demos showing how to call model wrappers and inspect raw outputs.

- `embedding/`
	- Placeholder for embedding generation and vector-store experiments (semantic search demos).

- Root files
	- `requirements.txt`: dependency manifest to reproduce the environment.

## How to run examples
1. Create a `.env` file with any provider keys required and a `USER_AGENT` when scraping:

```powershell
# .env example
GOOGLE_API_KEY=your_key_here
USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) ..."
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run example scripts (use forward slashes for cross-platform compatibility):

```bash
python document-loaders/txt.py
python document-loaders/webloader.py
python textsplitter/split_by_string_demo.py
```

- Note: The example scripts (e.g., `txt.py`, PDF loaders) require you to provide your own data files (for example, a `poem.txt` or PDF files) in the correct path before running.

## Known issues I encountered and fixed
- Dependency mismatches: I aligned `langchain-core` to compatible versions when packages required `>=1.0.0`.
- Prompt variable mismatches: I ensured `PromptTemplate.input_variables` matched keys passed to `invoke` (for example, pass `{"poem": text}` when the template uses `{poem}`).
- File path typos: corrected filenames (for example, `Wealthify_conferncepaper[1].pdf` → `Wealthify_conferencepaper[1].pdf`) or used absolute paths.
- TextSplitter API changes: removed unsupported constructor args (e.g., `language`, `separator`) and used the version-compatible signature.

## Next steps & suggestions
- Add small unit tests or sample runners for each folder to make it easier to reproduce experiments.
- Add a `requirements-dev.txt` with pinned package versions that are known to work together.
- Add an `.env.example` listing required environment variables (API keys, `USER_AGENT`).

---
Updated: merged README combining both versions, fixed typos, renamed splitter examples to avoid builtin shadowing, and converted paths to portable format.
# langchain