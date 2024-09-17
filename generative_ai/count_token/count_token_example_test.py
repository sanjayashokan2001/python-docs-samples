# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import compute_tokens_example
import count_token_example


def test_count_token() -> None:
    assert count_token_example.count_token_locally()
    assert count_token_example.count_token_service()


def test_compute_token() -> None:
    assert compute_tokens_example.compute_tokens_example()
